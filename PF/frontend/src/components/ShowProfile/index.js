import axios from 'axios';
import React, { useState, useEffect } from 'react'


function ShowProfile ()  {
    const [profiles, setProfile] = useState([{
        first_name: "",
        last_name: "",
        email: "",
        avatar: "",
        phone_num: "",
    }])
    useEffect(() => {
        const apiUrl1 = '/accounts/profile/';
        axios.get(apiUrl1).then((res) => {
            console.log(res.data)
            const {data} = res;
            setProfile(data);
        }).catch((error) => {
            if (error.response) {
                console.log(error.response)
            }
        })}, [])
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
                profiles?.map((profile, index) => (
                    <div key={index}>
                        <p>{profile.first_name}</p>
                        <p>{profile.last_name}</p>
                        <p>{profile.email}</p>
                        <p><img src={profile.avatar}/></p>
                        <p>{profile.phone_num}</p>
                        </div>
                ))
            }

        </div>
    )
}



export default ShowProfile