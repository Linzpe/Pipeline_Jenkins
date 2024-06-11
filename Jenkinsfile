pipeline {
    agent any
    
    stages {
        // Primer paso: checkout. Se descarga el repositorio completo en jenkins
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/WebGoat/WebGoat.git'
            }
        }
        
        // En esta etapa se cambian las versiones 21 por 17.
        stage('Update POM') {
            steps {
                // Usa 'sed' para cambiar todas las ocurrencias de '21' por '17' en el archivo pom.xml
                sh 'sed -i "s/<java.version>21<\\/java.version>/<java.version>17<\\/java.version>/g" pom.xml'
                sh 'sed -i "s/<maven.compiler.source>21<\\/maven.compiler.source>/<maven.compiler.source>17<\\/maven.compiler.source>/g" pom.xml'
                sh 'sed -i "s/<maven.compiler.target>21<\\/maven.compiler.target>/<maven.compiler.target>17<\\/maven.compiler.target>/g" pom.xml'
            }
        }
        
        // Segundo paso: Build. En el archivo pom.xml está la lista de archivos necesarios para crear el JAR o WAR.
        // Se limpia el directorio target y se compilan los archivos del Pom.xml
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
        
        // Tercer paso: Package. Empaqueta los archivos mediante "mvn package"
        stage('Package') {
            steps {
                sh 'mvn package'
            }
        }
        // Cuarto paso: Deploy. Despliega en un directorio local la aplicación generada
        stage('Deploy') {
            steps {
                script {
                    def deployDir = '/var/jenkins_home/aplicacion_WEBGOAT'
                    sh "mkdir -p ${deployDir}"
                    sh "cp target/webgoat-2024.2-SNAPSHOT.jar ${deployDir}"
                    sh "nohup java -jar ${deployDir}/webgoat-server-*.jar > ${deployDir}/webgoat.log 2>&1 &"
                }
            }
        }
    }
}

