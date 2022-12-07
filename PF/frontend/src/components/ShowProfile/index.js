import axios from 'axios';
import React, { useState, useEffect } from 'react'

const ShowProfile = () => {
    const [profiles, setProfile] = useState([])

    const getProfile = async () => {
        const response = await axios.get('http:localhost:8000/accounts/profile/')
        setProfile(response.data)
    }

    useEffect(() => {
        getProfile()
    }, [])

    return (
        <div>
            <h1>Show Profile Information</h1>
            {
                profiles.map((profile, index) => (
                    <div>
                        <p>{profile.first_name}</p>
                        <p>{profile.last_name}</p>
                        <p>{profile.email}</p>
                        <p>{profile.phone_num}</p>
                        </div>
                ))
            }

        </div>
    )
}



export default ShowProfile