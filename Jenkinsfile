pipeline {
    agent any
    
    stages {
        stage('Setup Python Environment') {
            steps {
                script {
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    
                    pip install playwright
                    PLAYWRIGHT_BROWSERS_PATH=~/.cache/ms-playwright playwright install chromium
                    PLAYWRIGHT_BROWSERS_PATH=~/.cache/ms-playwright playwright install firefox
                    PLAYWRIGHT_BROWSERS_PATH=~/.cache/ms-playwright playwright install webkit
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    pytest --alluredir=allure-results
                    '''
                }
            }
            post {
                always {
                    allure includeProperties:
                     false,
                     jdk: '',
                     results: [[path: 'allure-results']]
                }
            }
        }
        stage('Cleanup') {
            steps {
                script {
                    // remove env
                    sh '''
                    rm -rf venv
                    '''
                }
            }
        }
    }
}
