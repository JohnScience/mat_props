# Расчёт свойств материалов

Приложение состоит из двух частей:

1. `front` - статический фронтенд, написанный на [React](https://react.dev/) + Vanilla JavaScript и собираемый бандлером [Vite](https://vitejs.dev/).
2. `app` - кросс-платформенное приложение использующее фреймворк [Tauri](https://tauri.app/) и статический фронтенд.

## Сборка артефактов для установки

В данный момент, Tauri не поддерживает кросс-компиляцию, поэтому они должны собираться на целевой платформе или с помощью Docker (для Linux).

### Сборка для Linux (в Docker)

Можно собирать и на Windows.

```console
# Создаём Docker образ с именем "mat-props", в котором будет собрано приложение
docker build -t mat-props .
# Создаём одноиёменный контейнер, который будет ждать вечно (без `sleep infinity` на Windows происходит ошибка `Error response from daemon: No command specified`)
docker create --name mat-props mat-props sleep infinity
# Экспортируем файловую систему контейнера в tar-архив
docker export mat-props > mat-props-linux.tar
# Удаляем контейнер mat-props
docker container rm mat-props
# Удаляем образ mat-props
docker image rm mat-props
```

После этого в текущей директории появится файл `mat-props-linux.tar`, внутри которого по пути `usr/mat-props/` можно обнаружить три директории:

- `appimage` - с результатом сборки [AppImage-пакета](https://ru.wikipedia.org/wiki/AppImage).
- `deb` - с результатом сборки [deb-пакета](https://ru.wikipedia.org/wiki/Deb_(%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82_%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2))
- `msi` - с результатом сборки [msi-установщика](https://ru.wikipedia.org/wiki/Microsoft_Windows_Installer) для Windows.

### Сборка с помощью GitHub Actions

> В процессе разработки
