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
                            url: 'https://github.com/50gramx/eapp-python-domain.git'
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
    stage('Clean workspace') {
        cleanWs()
        echo "done"
    }
}
//
// step-1: deploy the pypi server
// step-2: build the package
// step-3: push the package