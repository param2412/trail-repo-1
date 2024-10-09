
Mc:/Users/lenovo/Desktop/New_React_Project/FireDeptWebApp/backend/utils/otp.js¿import crypto from 'crypto';
import nodemailer from 'nodemailer';
import Inspector from '../models/inspector.js';

export function generateOTP() {
    return crypto.randomInt(100000, 999999).toString(); // 6-digit OTP
}

export async function sendOTP(email, otp) {
    let transporter = nodemailer.createTransport({
        service: 'Gmail',
        auth: {
            user: 'param2412parikh@gmail.com',
            pass: 'your-email-password',
        },
    });

    let mailOptions = {
        from: 'your-email@gmail.com',
        to: email,
        subject: 'Your OTP Code',
        text: `Your OTP code is ${otp}`,
    };

    await transporter.sendMail(mailOptions);
}
… …”
”¿ "(be08188c6a813041d3f8263e055b76e7c045a601*8c:/Users/lenovo/Desktop/New_React_Project/FireDeptWebApp2Ufile:///c:/Users/lenovo/Desktop/New_React_Project/FireDeptWebApp/backend/utils/otp.js:@file:///c:/Users/lenovo/Desktop/New_React_Project/FireDeptWebApp