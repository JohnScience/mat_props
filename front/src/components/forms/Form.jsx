import React from "react";
import { ElasticModulesForUnidirectionalComposite } from "./ElasticModulesForUnidirectionalComposite";
import { ThermalExpansionForUnidirectionalComposite } from "./ThermalExpansionForUnidirectionalComposite";
import { ThermalConductivityForUnidirectionalComposite } from "./ThermalConductivityForUnidirectionalComposite";
import { ElasticModulesForHoneycomb } from "./ElasticModulesForHoneycomb";
import { ThermalExpansionForHoneycomb } from "./ThermalExpansionForHoneycomb";

export const Form = () => {
    const [fn, setFn] = React.useState("elastic_modules_for_unidirectional_composite");

    const handleChange = (event) => {
        setFn(event.target.value);
    }

    return (
        <>
            <div>
                <h1>Свойства материалов</h1>
            </div>
            <div>
                <label>
                    Функция <br />
                <select value={fn} onChange={handleChange}>
                    <option value="elastic_modules_for_unidirectional_composite">elastic_modules_for_unidirectional_composite</option>
                    <option value="thermal_expansion_for_unidirectional_composite">thermal_expansion_for_unidirectional_composite</option>
                    <option value="thermal_conductivity_for_unidirectional_composite">thermal_conductivity_for_unidirectional_composite</option>
                    <option value="elastic_modules_for_honeycomb">elastic_modules_for_honeycomb</option>
                    <option value="thermal_expansion_for_honeycomb">thermal_expansion_for_honeycomb</option>
                </select>
                </label>

                {
                    fn == "elastic_modules_for_unidirectional_composite" ?
                        <ElasticModulesForUnidirectionalComposite /> :
                    fn == "thermal_expansion_for_unidirectional_composite" ?
                        <ThermalExpansionForUnidirectionalComposite /> :
                    fn == "thermal_conductivity_for_unidirectional_composite" ?
                        <ThermalConductivityForUnidirectionalComposite /> :
                    fn == "elastic_modules_for_honeycomb" ?
                        <ElasticModulesForHoneycomb /> :
                    fn == "thermal_expansion_for_honeycomb" ?
                        <ThermalExpansionForHoneycomb /> :
                        null
                }
            </div>
        </>
    )
}