pipeline { 
    agent any

    environment {
        // Define repository details:
        REPO_URL = 'https://github.com/jimmyroa/devops.git'
        BRANCH = 'main'
    }
    
    // Configure triggers for GitHub webhook and periodic checks:
    triggers {
        // Trigger builds using GitHub webhooks for immediate reaction to updates
        githubPush()

        // Fallback: Poll for SCM changes every 2 minutes
        cron('H/2 * * * *')
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                // Checkout source code from SCM:
                checkout scm
            }
        }

        stage('Debug Batch Script') {
            steps {
                // Test setting global environment variables:
                bat '"C:\\Windows\\System32\\cmd.exe" /c echo %PATH%'
            }
        }
        
        stage('Build') {
            steps {
                script {
                    // Run the Python script:
                    bat 'python devops_a2.py'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Run the unit tests:
                    bat 'python test_employee_salary.py'
                }
            }
        }

        stage('Package') {
            steps {
                script {
                    // Install pyinstaller if not already installed:
                    bat 'pip install pyinstaller'
                    
                    // Create a standalone executable:
                    bat 'pyinstaller --onefile devops_a2.py'
                }
            }
        }
    }
    
    // Post-build actions
    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Build and tests succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
