const ENV_ROUTE = import.meta.env.VITE_API_URL;
export const API_ROUTE = ENV_ROUTE ? ENV_ROUTE : 'http://localhost:5000';

interface VerificationData {
    statusCode: number;
    data: any;
}

export async function VerifyJWT(token: string): Promise<VerificationData> {
    return fetch(`${API_ROUTE}/user/get_current_user/`, {
        method: "GET",
        headers: {
            Authorization: token,
        },
    })
    .then(async (res) => {
        const data = await res.json();
        return {
            statusCode: res.status,
            data: data,
        } as VerificationData;
    })
    .catch((err) => {
        console.log("VerifyJWT failed:", err);
        return { statusCode: 500, data: "" } as VerificationData;
    });
}