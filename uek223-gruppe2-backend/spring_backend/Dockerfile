# -------- BUILD STAGE --------
FROM gradle:8.5-jdk17 AS build

WORKDIR /app
COPY . .

# Build with Gradle (using container's gradle, no wrapper needed)
RUN gradle --no-daemon bootJar

# -------- RUNTIME STAGE --------
FROM amazoncorretto:17

WORKDIR /app
COPY --from=build /app/build/libs/*.jar app.jar

EXPOSE 8080

CMD ["java", "-jar", "-Xmx1g", "app.jar"]
