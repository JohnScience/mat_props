import React from "react";
import { Benchmark } from "../Benchmark";

export const ThermalExpansionForUnidirectionalComposite = () => {
    // Модель Ванина
    const numberOfModel = 1;

    const [fiberContent, setFiberContent] = React.useState(0.2);
    const [eForFiber, setEForFiber] = React.useState(100.0);
    const [nuForFiber, setNuForFiber] = React.useState(0.3);
    const [alphaForFiber, setAlphaForFiber] = React.useState(0.3);
    const [eForMatrix, setEForMatrix] = React.useState(5.0);
    const [nuForMatrix, setNuForMatrix] = React.useState(0.2);
    const [alphaForMatrix, setAlphaForMatrix] = React.useState(0.2);
    const [computedValues, setComputedValues] = React.useState(([],{secs: 0, nanos: 0}));

    function handleFiberContentChange(event) {
        setFiberContent(event.target.value);
    }

    function handleEForFiberChange(event) {
        setEForFiber(event.target.value);
    }

    function handleNuForFiberChange(event) {
        setNuForFiber(event.target.value);
    }

    function handleAlphaForFiberChange(event) {
        setAlphaForFiber(event.target.value);
    }

    function handleEForMatrixChange(event) {
        setEForMatrix(event.target.value);
    }

    function handleNuForMatrixChange(event) {
        setNuForMatrix(event.target.value);
    }

    function handleAlphaForMatrixChange(event) {
        setAlphaForMatrix(event.target.value);
    }

async function compute() {
    if (!window.__TAURI__) {
        console.error("Tauri API is not available in browser");
        return;
    }
    let response = await window.__TAURI__.invoke("thermal_expansion_for_unidirectional_composite", {
        numberOfModel: numberOfModel,
        fiberContent: fiberContent,
        eForFiber: eForFiber,
        nuForFiber: nuForFiber,
        alphaForFiber: alphaForFiber,
        eForMatrix: eForMatrix,
        nuForMatrix: nuForMatrix,
        alphaForMatrix: alphaForMatrix,
    });
    console.log(response);
    setComputedValues(response);
}

    return <>
        <form>
            <label>Доля объема волокон в композите (от 0 до 1):
                <input type="number" value={fiberContent} min="0" max="1" step="0.01" onChange={handleFiberContentChange} />
            </label>
            <br />
            <label>Модуль Юнга (E) для волокон:
                <input type="number" value={eForFiber} step="0.1" onChange={handleEForFiberChange} />
            </label>
            <br />
            <label>Коэффициент Пуассона (v) для волокон:
                <input type="number" value={nuForFiber} step="0.1" onChange={handleNuForFiberChange} />
            </label>
            <br />
            <label>Коэффициент линейного теплового расширения (α) для волокон:
                <input type="number" value={alphaForFiber} step="0.1" onChange={handleAlphaForFiberChange} />
            </label>
            <br />
            <label>Модуль Юнга (E) для матрицы:
                <input type="number" value={eForMatrix} step="0.1" onChange={handleEForMatrixChange} />
            </label>
            <br />
            <label>Коэффициент Пуассона (v) для матрицы:
                <input type="number" value={nuForMatrix} step="0.1" onChange={handleNuForMatrixChange} />
            </label>
            <br />
            <label>Коэффициент линейного теплового расширения (α) для матрицы:
                <input type="number" value={alphaForMatrix} step="0.1" onChange={handleAlphaForMatrixChange} />
            </label>
            <br />
            <input type="button" value="Рассчитать" onClick={compute} />

            { computedValues.length > 0 &&
                <>
                    <h2>Значения:</h2>
                    <p>α1 = {computedValues[0][0].toFixed(10)}</p>
                    <p>α2 = {computedValues[0][1].toFixed(10)}</p>
                    <p>α3 = {computedValues[0][2].toFixed(10)}</p>
                    <Benchmark t={computedValues[1]} />
                </>
            }

        </form>
    </>
}
