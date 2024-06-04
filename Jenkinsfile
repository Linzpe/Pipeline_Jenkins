pipeline {
    agent any
    
    stages {
        # Primer paso: checkout. Se descarga el repositorio completo en jenkins
        stage('Checkout') {
            steps {
                git 'https://github.com/WebGoat/WebGoat.git'
            }
        }
        # Segundo paso: Build. En el archivo pom.xml está la lista de archivos necesarios para crear el JAR o WAR.
        # Se limpia el directorio target y se compilan los archivos del Pom.xml
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
        # Tercer paso: Package. Empaqueta los archivos mediante "mvn package"
        stage('Package') {
            steps {
                sh 'mvn package'
            }
        }
        # Cuarto paso: Deploy. Despliega en un directorio local la aplicación generada
        stage('Deploy') {
            steps {
                sh 'mkdir -p /var/jenkins_home/aplicacion_WEBGOAT'
                sh 'cp target/webgoat-*.war /var/jenkins_home/aplicacion_WEBGOAT'
            }
        }
    }
}
