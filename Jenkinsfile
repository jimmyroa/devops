pipeline {
    agent any
    
    environment {
        // Python version to use
        PYTHON_VERSION = '3.x'
        // Virtual environment path
        VENV_PATH = "${WORKSPACE}/venv"
    }
    
    triggers {
        // GitHub webhook trigger for push events on main branch
        githubPush()

        // Optional: Periodic build every 4 hours (can be commented out if not needed)
        // cron('0 */4 * * *')
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout source code from SCM
                checkout scm
            }
        }
        
        stage('Set up Python') {
            steps {
                script {
                    // Set up Python environment
                    sh '''
                        python3 -m venv ${VENV_PATH}
                        . ${VENV_PATH}/bin/activate
                        python --version
                    '''
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV_PATH}/bin/activate
                    python -m unittest discover
                '''
            }
            post {
                always {
                    // Capture test results if using XML reports
                    junit allowEmptyResults: true, testResults: '**/test-*.xml'
                }
            }
        }
    }
    
    post {
        success {
            echo 'CI Pipeline completed successfully!'
        }
        failure {
            echo 'CI Pipeline failed. Check the logs for details.'
        }
        cleanup {
            // Clean up virtual environment
            sh '''
                rm -rf ${VENV_PATH}
            '''
        }
    }
}
