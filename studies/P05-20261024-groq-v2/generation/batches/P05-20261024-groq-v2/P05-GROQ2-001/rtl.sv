module p05 (
    input  logic clk,
    input  logic rst,
    input  logic req,
    output logic ack
);
    logic req_d;

    always_ff @(posedge clk) begin
        if (rst) begin
            req_d <= 1'b0;
        end else begin
            req_d <= req;
        end
    end

    assign ack = req_d;
endmodule
