FROM rust:latest as builder

RUN apt update && \
    apt install -y \
    libpython3-dev \
    libwebkit2gtk-4.0-dev \
    build-essential \
    curl \
    wget \
    file \
    libssl-dev \
    libgtk-3-dev \
    libayatana-appindicator3-dev \
    librsvg2-dev \
    npm && \
    cargo install tauri-cli


# Устанавливаем директорию для работы с приложением
WORKDIR /usr/mat-props/app/src-tauri

# Инициализируем пустой исполняемый проект для кеширования зависимостей
RUN cargo init --bin --name mat-props

# Копируем файлы с зависимостями для их установки
COPY ./app/src-tauri/Cargo.toml ./app/src-tauri/Cargo.lock ./

# Собираем приложение для установки зависимостей
RUN cargo build --release

# Копируем исходники приложения
COPY ./app/src-tauri /usr/mat-props/app/src-tauri

# Копируем исходники фронтенда
COPY ./front/ /usr/mat-props/front

# Устанавливаем WORKDIR для фронтенда
WORKDIR /usr/mat-props/front

# Устанавливаем зависимости фронтенда
RUN npm install

# Собираем фронтенд
RUN npm run build-for-app

# Устанавливаем директорию для работы с приложением
WORKDIR /usr/mat-props/app/src-tauri

# Собираем приложение повторно для создания необходимых артефактов сборки
RUN cargo tauri build

FROM scratch as final

WORKDIR /usr/mat-props/

COPY --from=builder /usr/mat-props/app/src-tauri/target/release/bundle /usr/mat-props/
