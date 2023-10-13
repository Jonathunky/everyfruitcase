export const config = {
  runtime: "edge",
}

export default async function handler(request) {
  try {
    const report = await request.json()
    console.log("CSP Report:", report)
    return new Response(null, { status: 204 })
  } catch (error) {
    console.error("Error processing CSP report:", error)
    return new Response("Error processing report", { status: 500 })
  }
}
