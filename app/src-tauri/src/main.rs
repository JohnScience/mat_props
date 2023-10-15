#![cfg_attr(
    all(not(debug_assertions), target_os = "windows"),
    windows_subsystem = "windows"
)]

use pyo3::types::PyTuple;

#[tauri::command]
fn see_funcs(app: tauri::AppHandle) -> (Vec<String>, std::time::Duration) {
    use pyo3::prelude::*;
    use pyo3::types::PyFunction;

    let before = std::time::Instant::now();
    let mat_props = app
        .path_resolver()
        .resolve_resource("resources/mat_props.py")
        .expect("failed to resolve resource");

    let mat_props = dunce::simplified(&mat_props).to_path_buf();

    let code = std::fs::read_to_string(mat_props).unwrap();
    let mut members = Vec::<String>::new();
    Python::with_gil(|py| -> PyResult<()> {
        // https://docs.python.org/3/library/inspect.html
        let inspect = PyModule::import(py, "inspect").unwrap();
        // from inspect import getmembers
        let get_members: &PyFunction = inspect.getattr("getmembers").unwrap().downcast().unwrap();
        // from inspect import isfunction
        let is_function = inspect.getattr("isfunction").unwrap();

        let mat_props = PyModule::from_code(py, &code, "mat_props.py", "mat_props").unwrap();

        // getmembers(mat_props, isfunction)
        let members_iter = get_members
            .call1((mat_props, is_function))
            .unwrap()
            .iter()
            .unwrap()
            .map(|tup| {
                let tup = tup.unwrap().downcast::<PyTuple>().unwrap();
                tup.get_item(0).unwrap().extract::<String>().unwrap()
            });
        members.extend(members_iter);
        Ok(())
    })
    .unwrap();
    let after = std::time::Instant::now();
    let diff = after - before;

    (members, diff)
}

// await window.__TAURI__.invoke("elastic_modules_for_unidirectional_composite", { numberOfModel: 2, fibreContent: 0.2, eForFiber: 100.0, nuForFiber: 0.3, eForMatrix: 5.0, nuForMatrix: 0.2 });
#[tauri::command]
fn elastic_modules_for_unidirectional_composite(
    app: tauri::AppHandle,
    number_of_model: u64,
    fibre_content: f64,
    e_for_fiber: f64,
    nu_for_fiber: f64,
    e_for_matrix: f64,
    nu_for_matrix: f64,
) -> ([f64; 9], std::time::Duration) {
    use pyo3::prelude::*;
    use pyo3::types::PyFunction;

    let before = std::time::Instant::now();
    let mat_props = app
        .path_resolver()
        .resolve_resource("resources/mat_props.py")
        .expect("failed to resolve resource");

    let mat_props = dunce::simplified(&mat_props).to_path_buf();

    let code = std::fs::read_to_string(mat_props).unwrap();
    let mut out = [0.0; 9];
    Python::with_gil(|py| -> PyResult<()> {
        let mat_props = PyModule::from_code(py, &code, "mat_props.py", "mat_props").unwrap();

        let elastic_modules_for_unidirectional_composite: &PyFunction = mat_props
            .getattr("Elastic_modules_for_unidirectional_composite")
            .unwrap()
            .downcast()
            .unwrap();

        out = elastic_modules_for_unidirectional_composite
            .call1((
                number_of_model,
                fibre_content,
                e_for_fiber,
                nu_for_fiber,
                e_for_matrix,
                nu_for_matrix,
            ))
            .unwrap()
            .extract::<[f64; 9]>()
            .unwrap();
        Ok(())
    })
    .unwrap();
    let after = std::time::Instant::now();
    let diff = after - before;

    (out, diff)
}

// await window.__TAURI__.invoke("thermal_expansion_for_unidirectional_composite", { numberOfModel: 1, fibreContent: 0.2, eForFiber: 100.0, nuForFiber: 0.3, alphaForFiber: 1e-6, eForMatrix: 5.0, nuForMatrix: 0.2, alphaForMatrix: 20e-5 })
#[tauri::command]
fn thermal_expansion_for_unidirectional_composite(
    app: tauri::AppHandle,
    number_of_model: u64,
    fibre_content: f64,
    e_for_fiber: f64,
    nu_for_fiber: f64,
    alpha_for_fiber: f64,
    e_for_matrix: f64,
    nu_for_matrix: f64,
    alpha_for_matrix: f64,
) -> ([f64; 3], std::time::Duration) {
    use pyo3::prelude::*;
    use pyo3::types::PyFunction;

    let before = std::time::Instant::now();
    let mat_props = app
        .path_resolver()
        .resolve_resource("resources/mat_props.py")
        .expect("failed to resolve resource");

    let mat_props = dunce::simplified(&mat_props).to_path_buf();

    let code = std::fs::read_to_string(mat_props).unwrap();
    let mut out = [0.0; 3];
    Python::with_gil(|py| -> PyResult<()> {
        let mat_props = PyModule::from_code(py, &code, "mat_props.py", "mat_props").unwrap();

        let elastic_modules_for_unidirectional_composite: &PyFunction = mat_props
            .getattr("Thermal_expansion_for_unidirectional_composite")
            .unwrap()
            .downcast()
            .unwrap();

        out = elastic_modules_for_unidirectional_composite
            .call1((
                number_of_model,
                fibre_content,
                e_for_fiber,
                nu_for_fiber,
                alpha_for_fiber,
                e_for_matrix,
                nu_for_matrix,
                alpha_for_matrix,
            ))
            .unwrap()
            .extract::<[f64; 3]>()
            .unwrap();
        Ok(())
    })
    .unwrap();
    let after = std::time::Instant::now();
    let diff = after - before;

    (out, diff)
}

// await window.__TAURI__.invoke("thermal_conductivity_for_unidirectional_composite", { numberOfModel: 2, fibreContent: 0.2, kForFiber: 100.0, kForMatrix: 1 })
#[tauri::command]
fn thermal_conductivity_for_unidirectional_composite(
    app: tauri::AppHandle,
    number_of_model: u64,
    fibre_content: f64,
    k_for_fiber: f64,
    k_for_matrix: f64,
) -> ([f64; 3], std::time::Duration) {
    use pyo3::prelude::*;
    use pyo3::types::PyFunction;

    let before = std::time::Instant::now();
    let mat_props = app
        .path_resolver()
        .resolve_resource("resources/mat_props.py")
        .expect("failed to resolve resource");

    let mat_props = dunce::simplified(&mat_props).to_path_buf();

    let code = std::fs::read_to_string(mat_props).unwrap();
    let mut out = [0.0; 3];
    Python::with_gil(|py| -> PyResult<()> {
        let mat_props = PyModule::from_code(py, &code, "mat_props.py", "mat_props").unwrap();

        let elastic_modules_for_unidirectional_composite: &PyFunction = mat_props
            .getattr("Thermal_conductivity_for_unidirectional_composite")
            .unwrap()
            .downcast()
            .unwrap();

        out = elastic_modules_for_unidirectional_composite
            .call1((number_of_model, fibre_content, k_for_fiber, k_for_matrix))
            .unwrap()
            .extract::<[f64; 3]>()
            .unwrap();
        Ok(())
    })
    .unwrap();
    let after = std::time::Instant::now();
    let diff = after - before;

    (out, diff)
}

// await window.__TAURI__.invoke("elastic_modules_for_honeycomb", { numberOfModel: 1, lCellSideSize: 9.24, hCellSideSize: 8.4619, wallThickness: 0.4, angle: Math.PI/6, eForHoneycomb: 7.07, nuForHoneycomb: 0.2 })
#[tauri::command]
fn elastic_modules_for_honeycomb(
    app: tauri::AppHandle,
    number_of_model: u64,
    l_cell_side_size: f64,
    h_cell_side_size: f64,
    wall_thickness: f64,
    angle: f64,
    e_for_honeycomb: f64,
    nu_for_honeycomb: f64,
) -> ([f64; 9], std::time::Duration) {
    use pyo3::prelude::*;
    use pyo3::types::PyFunction;

    let before = std::time::Instant::now();
    let mat_props = app
        .path_resolver()
        .resolve_resource("resources/mat_props.py")
        .expect("failed to resolve resource");

    let mat_props = dunce::simplified(&mat_props).to_path_buf();

    let code = std::fs::read_to_string(mat_props).unwrap();
    let mut out = [0.0; 9];
    Python::with_gil(|py| -> PyResult<()> {
        let mat_props = PyModule::from_code(py, &code, "mat_props.py", "mat_props").unwrap();

        let elastic_modules_for_honeycomb: &PyFunction = mat_props
            .getattr("Elastic_modules_for_honeycomb")
            .unwrap()
            .downcast()
            .unwrap();

        out = elastic_modules_for_honeycomb
            .call1((
                number_of_model,
                l_cell_side_size,
                h_cell_side_size,
                wall_thickness,
                angle,
                e_for_honeycomb,
                nu_for_honeycomb,
            ))
            .unwrap()
            .extract::<[f64; 9]>()
            .unwrap();
        Ok(())
    })
    .unwrap();
    let after = std::time::Instant::now();
    let diff = after - before;

    (out, diff)
}

// await window.__TAURI__.invoke("thermal_expansion_for_honeycomb", { numberOfModel: 1, lCellSideSize: 9.24, hCellSideSize: 8.4619, wallThickness: 0.4, angle: Math.PI/6, alphaForHoneycomb: 20e-5 })
#[tauri::command]
fn thermal_expansion_for_honeycomb(
    app: tauri::AppHandle,
    number_of_model: u64,
    l_cell_side_size: f64,
    h_cell_side_size: f64,
    wall_thickness: f64,
    angle: f64,
    alpha_for_honeycomb: f64,
) -> ([f64; 3], std::time::Duration) {
    use pyo3::prelude::*;
    use pyo3::types::PyFunction;

    let before = std::time::Instant::now();
    let mat_props = app
        .path_resolver()
        .resolve_resource("resources/mat_props.py")
        .expect("failed to resolve resource");

    let mat_props = dunce::simplified(&mat_props).to_path_buf();

    let code = std::fs::read_to_string(mat_props).unwrap();
    let mut out = [0.0; 3];
    Python::with_gil(|py| -> PyResult<()> {
        let mat_props = PyModule::from_code(py, &code, "mat_props.py", "mat_props").unwrap();

        let elastic_modules_for_honeycomb: &PyFunction = mat_props
            .getattr("Thermal_expansion_for_honeycomb")
            .unwrap()
            .downcast()
            .unwrap();

        out = elastic_modules_for_honeycomb
            .call1((
                number_of_model,
                l_cell_side_size,
                h_cell_side_size,
                wall_thickness,
                angle,
                alpha_for_honeycomb,
            ))
            .unwrap()
            .extract::<[f64; 3]>()
            .unwrap();
        Ok(())
    })
    .unwrap();
    let after = std::time::Instant::now();
    let diff = after - before;

    (out, diff)
}

fn main() {
    tauri::Builder::default()
        .setup(|_app| {
            // we can install Python before the application starts
            pyo3::prepare_freethreaded_python();
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![
            see_funcs,
            elastic_modules_for_unidirectional_composite,
            thermal_expansion_for_unidirectional_composite,
            thermal_conductivity_for_unidirectional_composite,
            elastic_modules_for_honeycomb,
            thermal_expansion_for_honeycomb,
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
