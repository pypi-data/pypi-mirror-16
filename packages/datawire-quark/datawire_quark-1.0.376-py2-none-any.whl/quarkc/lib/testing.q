quark *;
import quark.reflect;
import quark.concurrent;

namespace quark {
namespace test {

class TestInitializer extends TLSInitializer<Test> {
    Test getValue() { return null; }
}

String red(String str) {
    return "\x1b[31;1m" + str + "\x1b[0m";
}

String green(String str) {
    return "\x1b[32;1m" + str + "\x1b[0m";
}

String bold(String str) {
    return "\x1b[1m" + str + "\x1b[0m";
}

class Test {

    static TLS<Test> ctx = new TLS<Test>(new TestInitializer());

    static Test current() {
        return ctx.getValue();
    }

    String name;
    int checks = 0;
    List<String> successes = [];
    List<String> failures = [];

    Test(String name) {
        self.name = name;
    }

    bool match(List<String> filters) {
        if (filters == null || filters.size() == 0) {
            return true;
        }

        int idx = 0;
        while (idx < filters.size()) {
            String filter = filters[idx];
            if (name.find(filter) >= 0) {
                return true;
            }
            idx = idx + 1;
        }

        return false;
    }

    void start() {
        ctx.setValue(self);
    }

    void stop() {
        String result = name + " [" + checks.toString() + " checks, " + failures.size().toString() + " failures]";
        if (failures.size() > 0) {
            print(red(result));
        } else {
            print(bold(result));
        }
        int idx = 0;
        while (idx < successes.size()) {
            print(green("  PASS: " + successes[idx]));
            idx = idx + 1;
        }
        idx = 0;
        while (idx < failures.size()) {
            print(red("  FAIL: " + failures[idx]));
            idx = idx + 1;
        }
        ctx.setValue(null);
    }

    bool check(bool value, String message) {
        checks = checks + 1;
        if (value) {
            successes.add(message);
        } else {
            failures.add(message);
        }
        return value;
    }

    void fail(String message) {
        check(false, message);
    }

    void run() {}

}

class MethodTest extends Test {

    Class klass;
    Method method;

    MethodTest(Class klass, Method method) {
        super(klass.getName() + "." + method.getName());
        self.klass = klass;
        self.method = method;
    }

    void run() {
        Method setup = klass.getMethod("setup");
        Method teardown = klass.getMethod("teardown");

        Object test = klass.construct([]);
        if (setup != null) {
            setup.invoke(test, []);
        }
        method.invoke(test, []);
        if (teardown != null) {
            teardown.invoke(test, []);
        }
    }

}

bool check(bool value, String message) {
    return Test.current().check(value, message);
}

bool checkEqual(Object expected, Object actual) {
    return Test.current().check(expected == actual, "expected " + expected.toString() + " got " + actual.toString());
}

void fail(String message) {
    Test.current().check(false, message);
}

bool checkOneOf(List<Object> expected, Object actual) {
    String message = "Expected one of [";
    int idx = 0;
    while (idx < expected.size()) {
        if (idx != 0) {
            message = message + ", ";
        }
        message = message + expected[idx].toString();
        if (expected[idx] == actual) {
            return check(true, "");
        }
        idx = idx + 1;
    }
    fail(message + "] got " + actual.toString());
    return false;
}

class Harness {

    String pkg;
    List<Test> tests = [];
    int filtered = 0;

    Harness(String pkg) {
        self.pkg = pkg;
    }

    void collect(List<String> filters) {
        List<String> names = Class.classes.keys();
        names.sort();
        int idx = 0;
        String pfx = pkg + ".";
        while (idx < names.size()) {
            String name = names[idx];
            if (name.startsWith(pfx) && name.endsWith("Test")) {
                Class klass = Class.get(name);
                List<Method> methods = klass.getMethods();
                int jdx = 0;
                while (jdx < methods.size()) {
                    Method meth = methods[jdx];
                    String mname = meth.getName();
                    if (mname.startsWith("test") && meth.getParameters().size() == 0) {
                        Test test = new MethodTest(klass, meth);
                        if (test.match(filters)) {
                            tests.add(test);
                        } else {
                            filtered = filtered + 1;
                        }
                    }
                    jdx = jdx + 1;
                }
            }
            idx = idx + 1;
        }
    }

    void list() {
        int idx = 0;
        while (idx < tests.size()) {
            Test test = tests[idx];
            print(test.name);
            idx = idx + 1;
        }
    }

    @doc("Run the tests, return number of failures.")
    int run() {
        print(bold("=============================== starting tests ==============================="));

        int idx = 0;
        int failures = 0;
        while (idx < tests.size()) {
            Test test = tests[idx];
            test.start();
            test.run();
            test.stop();
            if (test.failures.size() > 0) {
                failures = failures + 1;
            }
            idx = idx + 1;
        }
        int passed = tests.size() - failures;

        print(bold("=============================== stopping tests ==============================="));
        String result = "Total: " + (tests.size() + filtered).toString() +
            ", Filtered: " + filtered.toString() +
            ", Passed: " + passed.toString() +
            ", Failed: " + failures.toString();

        if (failures > 0) {
            print(red(result));
        } else {
            print(green(result));
        }
        return failures;
    }

    void json_report() {
        print("=============================== json report ===============================");

        int idx = 0;
        JSONObject report = new JSONObject();
        while (idx < tests.size()) {
            JSONObject item = new JSONObject();
            Test test = tests[idx];
            int f = 0;
            JSONObject failures = new JSONObject();
            while (f < test.failures.size()) {
                failures.setListItem(f, test.failures[f]);
                f = f + 1;
            }
            item["name"] = test.name;
            item["checks"] = test.checks;
            item["failures"] = failures;
            report.setListItem(idx, item);
            idx = idx + 1;
        }
        print(report.toString());
    }
}

void run(List<String> args) {
    String pkg = args[0];
    List<String> filters = [];
    bool list = false;
    bool json = false;
    int idx = 1;
    while (idx < args.size()) {
        String arg = args[idx];
        if (arg == "-l") {
            list = true;
        } else {
            if (arg == "--json") {
                json = true;
            } else {
                filters.add(arg);
            }
        }
        idx = idx + 1;
    }
    Harness h = new Harness(pkg);
    h.collect(filters);
    if (list) {
        h.list();
    } else {
        print(bold("Running: " + " ".join(args)));
        int failures = h.run();
        if (json) {
            h.json_report();
        }
        if (failures > 0) {
            Context.runtime().fail("Test run failed.");
        }
    }
}

macro bool isJavascript() $java{false} $py{False} $rb{false} $js{true};

}}
