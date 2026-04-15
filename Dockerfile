FROM maven:3.9.9-eclipse-temurin-17 AS build
WORKDIR /workspace
COPY pom.xml .
COPY src ./src
RUN mvn -B package -DskipTests

FROM eclipse-temurin:17-jre-jammy
WORKDIR /app
COPY --from=build /workspace/target/digital-wallet-system-1.0-SNAPSHOT.jar ./digital-wallet-system-1.0-SNAPSHOT.jar
ENTRYPOINT ["java", "-jar", "digital-wallet-system-1.0-SNAPSHOT.jar"]
