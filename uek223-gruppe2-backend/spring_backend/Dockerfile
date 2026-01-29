# -------- BUILD STAGE --------
FROM amazoncorretto:17 AS build

WORKDIR /app
COPY . .

# Build with Gradle
RUN chmod +x ./gradlew && ./gradlew --no-daemon bootJar

# -------- RUNTIME STAGE --------
FROM amazoncorretto:17

WORKDIR /app
COPY --from=build /app/build/libs/*.jar app.jar

EXPOSE 8080

CMD ["java", "-jar", "-Xmx1g", "app.jar"]
