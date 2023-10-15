import React from "react";
import { Benchmark } from "../Benchmark";

export const ThermalConductivityForUnidirectionalComposite = () => {
    const [numberOfModel, setNumberOfModel] = React.useState(1);
    const [fiberContent, setFiberContent] = React.useState(0.2);
    const [kForFiber, setKForFiber] = React.useState(100.0);
    const [kForMatrix, setKForMatrix] = React.useState(5.0);
    const [computedValues, setComputedValues] = React.useState(([],{secs: 0, nanos: 0}));
    
    function handleNumberOfModelChange(event) {
        setNumberOfModel(event.target.value);
    }

    function handleFiberContentChange(event) {
        setFiberContent(event.target.value);
    }

    function handleKForFiberChange(event) {
        setKForFiber(event.target.value);
    }

    function handleKForMatrixChange(event) {
        setKForMatrix(event.target.value);
    }

    async function compute() {
        if (!window.__TAURI__) {
            console.error("Tauri API is not available in browser");
            return;
        }
        let response = await window.__TAURI__.invoke("thermal_conductivity_for_unidirectional_composite", {
            numberOfModel: parseInt(numberOfModel),
            fiberContent: fiberContent,
            kForFiber: kForFiber,
            kForMatrix: kForMatrix,
        });
        console.log(response);
        setComputedValues(response);
    }

    return <>
        <form>
            <label>Модель:
                <select value={numberOfModel} onChange={handleNumberOfModelChange}>
                    <option value="1">Правило смеси</option>
                    <option value="2"> Модель Ванина</option>
                </select>
            </label>
            <br />
            <label>Доля объема волокон в композите (от 0 до 1):
                <input type="number" value={fiberContent} min="0" max="1" step="0.01" onChange={handleFiberContentChange} />
            </label>
            <br />
            <label>Коэффициент теплопроводности (K) для волокон:
                <input type="number" value={kForFiber} step="0.1" onChange={handleKForFiberChange} />
            </label>
            <br />
            <label>Коэффициент теплопроводности (K) для матрицы:
                <input type="number" value={kForMatrix} step="0.1" onChange={handleKForMatrixChange} />
            </label>
            <br />
            <input type="button" value="Рассчитать" onClick={compute} />

            { computedValues.length > 0 &&
                <>
                    <h2>Значения:</h2>
                    <p>K1 = {computedValues[0][0].toFixed(10)}</p>
                    <p>K2 = {computedValues[0][1].toFixed(10)}</p>
                    <p>K3 = {computedValues[0][2].toFixed(10)}</p>
                    <Benchmark t={computedValues[1]} />
                </>
            }

        </form>
    </>
}
