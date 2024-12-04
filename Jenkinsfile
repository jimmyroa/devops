pipeline {
    agent any

     environment {
        // Define repository details:
        REPO_URL = 'https://github.com/jimmyroa/devops.git'
        BRANCH = 'main'
    }
    
    // Configure triggers for GitHub webhook and periodic checks
    triggers {
        // GitHub webhook trigger for push events:
        githubPush()
        
        // Optional: Periodic build every 4 hours
        // cron('0 */4 * * *')
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                // Checkout source code from SCM:
                checkout scm
            }
        }

        /*stage('Debug PATH') {
            steps {
                bat 'echo %PATH%'
            }
        }*/
        
         stage('Debug Batch Script') {
            steps {
                // bat 'type C:\\WINDOWS\\TEMP\\jenkins*.bat' // ERROR
                // bat '"C:\\Windows\\System32\\cmd.exe" /c type C:\\WINDOWS\\TEMP\\jenkins*.bat' // ERROR
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
                    // Run the unit tests
                    bat 'python test_employee_salary.py'
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
