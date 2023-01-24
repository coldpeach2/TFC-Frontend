import { Tabs, Box } from '@mui/material'
import {Link, Outlet} from "react-router-dom";
import { useState } from 'react';
import './style.css'

const NavBar = () => {
    const [value, setValue] = useState(0)
    const handleChange = (event, newValue) => {
        setValue(newValue);
      }
    return (
        <Box sx={{ width: '100%' }}>
        <nav
        value={value}
        onChange={handleChange}>
        <Link to="/profile">View Profile</Link>
        <Link to="/profile/update/">Update Profile</Link>
        <Link to="/subscribe/">Subscribe</Link>
        <Link className="split" to="/logout/">Logout</Link>
        
        </nav>
        <Outlet />
      </Box>

    )
}
export default NavBar