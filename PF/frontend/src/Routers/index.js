import {BrowserRouter, Route, Routes} from "react-router-dom";
import ShowProfile from "../components/ShowProfile";

const Router = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<ShowProfile />}>
                </Route>
            </Routes>
        </BrowserRouter>
    )
}
export default Router