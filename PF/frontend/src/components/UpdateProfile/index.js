import { useState } from 'react'

function UpdateProfile() {
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [email, setEmail] = useState("")
    const [avatar, setAvatar] = useState(null)
    const [phoneNum, setPhoneNum] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post(user);
      }

      return (
        <>
        <section>
            <form onSubmit={handleSubmit}>
                <TextField fullWidth
                    id='firstName'
                    label='first name'
                    placeholder="Enter your name"
                    autoFocus
                    onChange={(e) => setFirstName(e.target.value)}
                    value={firstName}
                    />
                <TextField fullWidth
                    id='lastName'
                    label='last name'
                    placeholder="Enter your last name"
                    autoFocus
                    onChange={(e) => setLastName(e.target.value)}
                    value={lastName}
                     />

                <TextField fullWidth
                    id='email'
                    label='email'
                    placeholder="Enter your email"
                    /* error={validEmail ? "false" : "true"} */
                    autoFocus
                    onChange={(e) => setEmail(e.target.value)}
                    value={email}
                     />
                <TextField fullWidth
                    id='phoneNum'
                    label='phone number'
                    placeholder="Enter your phone number"
                    autoFocus
                    onChange={(e) => setPhoneNum(e.target.value)}
                    value={phoneNum}
                    />
                <input type="file"
                    id="avatar"
                    onChange={(e) => setAvatar(e.target.files[0])}
                    accept=".png, .jpg, .jpeg" />
                <Button type='submit' variant='contained' color='primary'>
                    Edit Profile
                </Button>
            </form>
        </section>
    </>
    )
}

export default UpdateProfile