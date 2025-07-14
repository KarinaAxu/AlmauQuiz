pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        DJANGO_SETTINGS_MODULE = 'AlmauQuiz.settings' // если нужно переопределить
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt || true'
            }
        }

        stage('Run Migrations') {
            steps {
                sh './venv/bin/python manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/python manage.py test'
            }
        }

        stage('Collect Static') {
            steps {
                sh './venv/bin/python manage.py collectstatic --noinput'
            }
        }

        // Можно добавить деплой или публикацию артефактов
    }

    post {
        always {
            echo 'Pipeline complete.'
        }
        failure {
            echo '❌ Build failed.'
        }
    }
}
  
