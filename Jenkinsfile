pipeline {
    agent any

    parameters {
        string(name: 'branch', defaultValue: 'main', description: 'Branch to build from')
        string(name: 'url', defaultValue: 'https://google.com', description: 'URL to test')
        string(name: 'path', defaultValue: '/Users/rustemsamoilenko/Desktop/roflan_ebLA', description: 'Path to test directory')
        string(name: 'marker', defaultValue: '', description: 'Parameters for pytest mark')
    }

    stages {
        stage('SCM') {
            steps {
                // Assuming you have already configured your Git repository in Jenkins
                checkout([$class: 'GitSCM', branches: [[name: "*/${params.branch}"]]])
            }
        }

        stage('Test Repo Setup') {
            steps {
                script {
                    // Give execution permissions to your install script if needed
                    // sudo chmod +x install.sh
                }
            }
        }

        stage('Test Run') {
            steps {
                script {
                    def markerOption = params.marker ? "-m ${params.marker}" : ""
                    def testCommand = "./run.sh ${markerOption} --url ${params.url} ${params.path}"
                    sh "pip install -r requirements.txt"
                    sh testCommand
                }
            }
        }
    }
}
