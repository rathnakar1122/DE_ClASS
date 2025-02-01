pipeline {
    agent any

    environment {
        // Define the path to your service account key file
        GOOGLE_APPLICATION_CREDENTIALS = 'C:\\ENV\\rathnakar-18m85a0320-hiscox-0d1ad7b79faf.json'
    }

    stages {
        stage('Setup GCloud') {
            steps {
                script {
                    // Authenticate with Google Cloud
                    sh """
                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                    gcloud config set project <your-project-id>
                    """
                }
            }
        }
        stage('Create GCS Bucket') {
            steps {
                script {
                    def bucketName = "my-jenkins-bucket-${UUID.randomUUID().toString()}"
                    sh """
                    gcloud storage buckets create $bucketName --location=us-central1
                    echo "Bucket $bucketName created successfully."
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Job completed."
        }
    }
}
