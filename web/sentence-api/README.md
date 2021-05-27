# Register

| Method | address        | description                       |
| ------ | -------------- | --------------------------------- |
| POST   | /auth/register | register a new user on the system |

## Registration flow

1. user will provide the following information for account creation

```json
 {
     full_name: string,
     username: string,
     password: string,
     email: string
 }
```

2. verify the req_body coming from the user
3. hash the password
4. create the user

   - When the user is created `is_verified: false` is added to indicate the user hasn't validated the account
   - We generate a verification link the will have a verification token

```json
{
    full_name: string,
    username: string,
    password: string,
    email: string,
    is_verified: boolean,
    sentence: {
        limit: number, // amount of sentences allocated 
        used: number // the amount of sentences used by the user
    }
}
   ```

5. send out a verification email

 Response:

 ```json
   {
    status: number,
    message: string
   }
 ```
 
6. after verification send back a jwt token

| Method | address             | description                                 |
| ------ | ------------------- | ------------------------------------------- |
| POST   | /auth/verify/:token | verify users email and activate the account |

```json
{
    access_token: string, // one hour expiration time
    refresh_token: string  // forever but changes when access_token is refreshed
}
```
