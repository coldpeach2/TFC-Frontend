import {BrowserRouter, Route, Routes} from "react-router-dom";
import ShowProfile from "../components/ShowProfile";

const Router = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/">
                    <Route path="profile" element={<ShowProfile />} />
                    {/* <Route path="converter" element={<Convert />} />
                    <Route path="players" element={<Players />} /> */}
                </Route>
            </Routes>
        </BrowserRouter>
    )
}
export default Router