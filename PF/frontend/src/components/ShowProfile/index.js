import axios from 'axios';
import React, { useState, useEffect } from 'react'


function ShowProfile ()  {
    const [profiles, setProfile] = useState([])
    useEffect(() => {
        const apiUrl1 = 'http:localhost:8000/accounts/profile/';
        fetch(apiUrl1).then((res) => {
            const {data} = res;
            setProfile(data);
        }).catch((error) => {
            if (error.response) {
                console.log(error.response)
            }
        })})
/*     const getProfile = async () => {
       await axios.get('http:localhost:8000/accounts/profile/').then((response) => {
            setProfile(response.data)
        }).catch((error) => {
            if( error.response ){
                console.log(error.response.data); // => the response payload 
            }
        });
            useEffect(() => {
        getProfile()
    }, [])
    } */



    return (
        <div>
            <h1>Show Profile Information</h1>
            {
                profiles.map((profile) => (
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