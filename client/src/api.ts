const ENV_ROUTE = import.meta.env.VITE_API_URL;
export const API_ROUTE = ENV_ROUTE ? ENV_ROUTE : 'http://localhost:8000';

interface VerificationData {
    statusCode: number;
    result: any;
}

export async function VerifyJWT(token: string): Promise<VerificationData> {
    return fetch(`${API_ROUTE}/user/get_current_user/`, {
        method: "GET",
        headers: {
            Authorization: token,
        },
    })
    .then((res) => {
        return {
            statusCode: res.status,
            result: res,
        } as VerificationData;
    })
    .catch((err) => {
        console.log("VerifyJWT failed:", err);
        return { statusCode: 500, result: "" } as VerificationData;
    });
}