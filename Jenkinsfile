pipeline {
    agent any
    

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: '3043e08d-b58f-4752-8015-5d68ed6f2df4', url: 'https://github.com/aceton41k/template-framework-py.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    // Создание виртуального окружения
                    sh '''
                    python3 -m venv venv
                    '''
                
                    // Активируем виртуальное окружение и устанавливаем зависимости
                    sh '''
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
                    // Активируем виртуальное окружение и запускаем тесты
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
