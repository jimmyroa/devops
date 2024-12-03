pipeline {
    agent any

     environment {
        // Define repository details
        REPO_URL = 'https://github.com/jimmyroa/devops.git'
        BRANCH = 'main'
    }
    
    // Configure triggers for GitHub webhook and periodic checks
    triggers {
        // GitHub webhook trigger for push events
        githubPush()
        
        // Optional: Periodic build every 4 hours (can be commented out if not needed)
        // cron('0 */4 * * *')
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                // Checkout source code from SCM:
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                script {
                    // Basic build steps (customize as needed)
                    sh 'python3 --version'
                    sh 'pip3 --version'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Add your test commands here
                    sh 'echo "Running tests..."'
                    // Example: sh 'python3 -m unittest discover'
                }
            }
        }
    }
    
    // Post-build actions
    post {
        success {
            echo 'Build successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
