pipeline {
    // use Docker as agent
    // use Docker as agent
    agent {
        docker {
            // Docker file attached below. Image pushed to dockerhub
            image 'efimovaleksey/mlops:stable'
            args '-u root:sudo '
        }
    }

    stages {
        stage('prepare_repo') {
            steps {
		dir("server") {
                	sh "python3 -m venv venv"
                	sh ". venv/bin/activate"
                	sh "pip3 install -r requirements.txt"
              
			sh "dvc remote modify myremote --local gdrive_user_credentials_file gdrive.json" 
			  withCredentials([file(credentialsId: 'gdrive', variable: 'gdrive')]) {
		    	  sh "cp \$gdrive $WORKSPACE"
                	}
 
                	withCredentials([file(credentialsId: 'env', variable: 'env')]) {
                    	  sh "cp \$env $WORKSPACE"
                	}
		}

                sh "ls -la"
            }
        }

	stage('dvc_data_get') {
	     steps {
		sh "dvc pull"
	     }
	}

	stage('flake8_test') {
	     steps {
		sh "flake8 server/"
	     }
	}

	stage('testing') {
	     steps {
		sh "python -m unittest discover -s server -p 'test_*.py'"
	    }
	}
    }
}
