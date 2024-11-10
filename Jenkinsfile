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
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd mygame
                python3 game.py --name "Christian" --choice "Rock"
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