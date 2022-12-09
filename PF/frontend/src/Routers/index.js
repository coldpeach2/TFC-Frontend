import {BrowserRouter, Route, Routes} from "react-router-dom";
/* import ShowProfile from "../components/ShowProfile"; */
import Login from "../components/Login";

const Router = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Login />}>
                </Route>
            </Routes>
        </BrowserRouter>
    )
}
export default Router