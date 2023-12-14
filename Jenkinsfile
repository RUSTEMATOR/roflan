pipeline {
    agent any

    parameters {
        string(name: 'branch', defaultValue: 'main', description: 'Git branch to build from')
        string(name: 'url', defaultValue: 'https://google.com', description: 'URL of the website to test')
        string(name: 'path', defaultValue: '/Users/rustemsamoilenko/Desktop/roflan_ebLA', description: 'Path to the directory or file containing tests')
        string(name: 'marker', defaultValue: '', description: 'Parameters for pytest marker')
    }

    stages {
        stage('SCM Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "*/${params.branch}"]]])
            }
        }

        stage('Test Repo Setup') {
            steps {
                #!/bin/bash
                sh 'chmod +x install.sh'
                sh './install.sh'
            }
        }

        stage('Install Dependencies') {
                steps {
                    dir('/Users/rustemsamoilenko/Desktop/Playwright/Deposit_bible')
                    script {
                        sh 'pip3 install -r requirements.txt'  // Replace with the actual path to your requirements.txt
                    }
                }
            }
        
        stage('Run Tests') {
            steps {
                script {
                    def markerOption = params.marker ? "-m ${params.marker}" : ""
                    sh 'chmod +x run_unix.sh'
                    sh 'export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/Library/Frameworks/Python.framework/Versions/3.11/bin:$PATH'
                    sh "./run_unix.sh -m ${markerOption} --url ${params.url} ${params.path}"
                }
            }
        }
    }
}
