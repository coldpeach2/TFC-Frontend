import axios from 'axios';
import React, { useState, useEffect } from 'react'
import { List, ListItem, ListItemText, Paper, Avatar, Typography, TextField, Button } from '@mui/material'

function Profile() {
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [email, setEmail] = useState("")
    const [avatar, setAvatar] = useState(null)
    const [phoneNum, setPhoneNum] = useState("")

    useEffect(() => {
        const apiUrl1 = '/accounts/profile/';
        axios.get(apiUrl1).then((res) => {
            const { data } = res;
            setFirstName(data.first_name)
            setLastName(data.last_name)
            setEmail(data.email)
            setPhoneNum(data.phone_num)
        }).catch((error) => {
            if (error.response) {
                console.log(error.response)
            }
        })
    }, [])

    return (
        <div>
            <h1>Profile</h1>
            <List>
                <ListItem>
                    <ListItemText primary={firstName} />
                    <ListItemText primary={lastName} />
                    <ListItemText primary={email} />
                    <ListItemText primary={phoneNum} />
                </ListItem>
            </List>


        </div>
    )
}



export default Profile