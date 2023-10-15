export const Benchmark = ({t: {secs: s, nanos: ns}}) => {

    return (
        <p>Вычислено за {s}с {Math.floor(ns / 1e6)}мс {Math.floor((ns % 1e6) / 1e3)}мкс {ns % 1e3}нс</p>
    )
}