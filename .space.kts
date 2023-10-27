import java.time.LocalDate

job("Python Capability Behaviour Acceptance") {

	startOn {
        gitPush {
            anyBranchMatching {
                +"release/*"
                +"master"
                +"main"
            }
        }
    }

    // check out eapp-service-core to /mnt/space/work/eapp-service-core
    git("eapp-service-core")

	parameters {
      text("EAPP_CORE_DOMAIN_DIR", value = "/mnt/space/work/eapp-service-core")
      text("EAPP_PYTHON_DOMAIN_DIR", value = "/mnt/space/work/eapp-python-domain")
    }

    container(displayName = "Run Python Domain Capability Contract Behaviour Tests", image = "python:3.9.16") {

        // load up all required paths in environments
        env["EAPP_CORE_DOMAIN_DIR"] = "{{ EAPP_CORE_DOMAIN_DIR }}"
        env["EAPP_PYTHON_DOMAIN_DIR"] = "{{ EAPP_PYTHON_DOMAIN_DIR }}"

        // start execution
        shellScript {
          content = """

            echo "install the environment dependencies"
            pip install -r ${'$'}EAPP_PYTHON_DOMAIN_DIR/requirements.txt
            # end of execution installing the environment dependencies

            echo "copy steps"
            cp -rf \
                ${'$'}EAPP_PYTHON_DOMAIN_DIR/src/tests/ethos/elint/services/product/identity/account/access_account/steps \
                ${'$'}EAPP_CORE_DOMAIN_DIR/src/main/features/ethos/elint/services/product/identity/account/access_account/features
            # end of copying steps

            echo "start tests"
            behave ${'$'}EAPP_CORE_DOMAIN_DIR/src/main/features/ethos/elint/services/product/identity/account/access_account/features
            # end of running tests

          """
        }   // end of execution

    }   // end of running Python Domain Capability Contract Behaviour Tests
}