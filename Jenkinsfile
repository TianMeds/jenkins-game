pipeline {
    agent { 
        node {
            label 'docker-agent-game-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd mygame
                git pull origin master
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd mygame
                python3 game.py --choice "Rock"
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}