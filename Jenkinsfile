pipeline {
    agent any

    environment {
        DJANGO_SETTINGS_MODULE = 'alma_statistics.settings'
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
                sh './venv/bin/pip install -r requirements.txt'
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
