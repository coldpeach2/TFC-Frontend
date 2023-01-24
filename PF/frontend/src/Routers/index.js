import {BrowserRouter, Route, Routes} from "react-router-dom";
import Profile from "../components/ShowProfile"; 
import Login from "../components/Login";
import Register from "../components/Register";
import NavBar from "../components/NavBar";
import Logout from "../components/Logout";

const Router = () => {
    return (
        <BrowserRouter>
            <Routes>
                {/* public routes */}
                <Route path="login" element={<Login />}></Route>
                <Route path="register" element={<Register/>}></Route>
                {/* user auth routes */}
                <Route path="/" element={<NavBar />}></Route>
                <Route path="profile" element={<Profile/>}></Route>
                <Route path="logout" element={<Logout/>}></Route>
                <Route path="subscribe" element={<Profile/>}></Route>
                <Route path="profile/update" element={<Profile/>}></Route>
                {/* user subscription routes */}
                <Route path="subscription/history" element={<Logout/>}></Route>
                <Route path="subscription/update" element={<Profile/>}></Route>

            </Routes>
        </BrowserRouter>
    )
}
export default Router