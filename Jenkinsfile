node {
    stage('Clean workspace') {
        cleanWs()
        echo "done"
    }
    stage('Checkout Python Domain') {
        dir('eapp-python-domain') {
            checkout(
                [
                    $class: 'GitSCM',
                    branches: [
                        [
                            name: '*/master'
                        ]
                    ],
                    extensions: [],
                    userRemoteConfigs: [
                        [
                            credentialsId: 'multiverse-delivery-github-50gramx',
                            url: 'https://Amit-Khetan-70@github.com/50gramx/eapp-python-domain.git'
                        ]
                    ]
                ]
            )
        }
        echo "done"
    }
    stage('Host Python Package Index') {
        withKubeConfig(
            clusterName: 'microk8s-cluster',
            contextName: 'microk8s',
            credentialsId: 'multiverse-india-do-config',
            namespace: 'multiverse-delivery',
            serverUrl: 'https://157.245.106.167:16443') {
            sh 'kubectl apply -f ${WORKSPACE}/eapp-python-domain/playbook/deployment.yaml'
            sh 'kubectl apply -f ${WORKSPACE}/eapp-python-domain/playbook/service.yaml'
        }
        echo "done"
    }
    stage('Build & Publish the Package') {
        sh '''
        #!/bin/sh

        cp ${WORKSPACE}/eapp-python-domain/pypirc ~/.pypirc
        cd ${WORKSPACE}/eapp-python-domain && python3 setup.py sdist register -r local upload -r local
        rm ~/.pypirc
        '''
    }
    stage('Clean workspace') {
        cleanWs()
        echo "done"
    }
}