import React from "react";
import { Benchmark } from "../Benchmark";



export const ThermalExpansionForHoneycomb = () => {
    const numberOfModel = 1;
    // Internally, the only available model ignores the wall thickness,
    // so it's not one of the inputs.
    const wallThickness = -1.0;
    const [lCellSideSize, setLCellSideSize] = React.useState(9.24);
    const [hCellSideSize, setHCellSideSize] = React.useState(8.4619);
    const [angle, setAngle] = React.useState(Math.PI / 6);
    const [alphaForHoneycomb, setAlphaForHoneycomb] = React.useState(0.2);
    const [computedValues, setComputedValues] = React.useState(([],{secs: 0, nanos: 0}));

    function handleLCellSideSizeChange(event) {
        setLCellSideSize(event.target.value);
    }

    function handleHCellSideSizeChange(event) {
        setHCellSideSize(event.target.value);
    }
    function handleAngleChange(event) {
        setAngle(event.target.value);
    }
    
    function handleAlphaForHoneycombChange(event) {
        setAlphaForHoneycomb(event.target.value);
    }

    async function compute() {
        if (!window.__TAURI__) {
            console.error("Tauri API is not available in browser");
            return;
        }
        let response = await window.__TAURI__.invoke("thermal_expansion_for_honeycomb", {
            numberOfModel: numberOfModel,
            lCellSideSize: lCellSideSize,
            hCellSideSize: hCellSideSize,
            wallThickness: wallThickness,
            angle: angle,
            alphaForHoneycomb: alphaForHoneycomb,
        });
        console.log(response);
        setComputedValues(response);
    }

    return <>
        <form>
            <label>Размер ячейки в длину:
                <input type="number" value={lCellSideSize} step="0.1" onChange={handleLCellSideSizeChange} />
            </label>
            <br />
            <label>Размер ячейки в высоту:
                <input type="number" value={hCellSideSize} step="0.1" onChange={handleHCellSideSizeChange} />
            </label>
            <br />
            <label>Угол между горизонталью и наклонной стенкой ячейки соты (в радианах):
                <input type="number" value={angle} step="0.1" onChange={handleAngleChange} />
            </label>
            <br />
            <label>Коэффициент теплового расширения (α) для материала соты:
                <input type="number" value={alphaForHoneycomb} step="0.1" onChange={handleAlphaForHoneycombChange} />
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
