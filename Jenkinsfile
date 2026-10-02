pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                echo 'Mengambil kode dari GitHub...'
            }
        }

        stage('2. Run Test') {
            steps {
                echo 'Menjalankan Unit Test Python...'
                // Menjalankan script test
                sh 'python3 test_app.py'
            }
        }

        stage('3. Run App') {
            steps {
                echo 'Menjalankan Aplikasi...'
                sh 'python3 app.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline Sukses! Semua tes lulus.'
        }
        failure {
            echo 'Pipeline Gagal! Ada kesalahan kode.'
        }
    }
}