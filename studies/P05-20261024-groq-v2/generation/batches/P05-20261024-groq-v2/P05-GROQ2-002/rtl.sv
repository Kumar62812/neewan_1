module p05 (
    input  logic clk,
    input  logic rst,
    input  logic req,
    output logic ack
);
    // Register to hold the sampled request
    logic req_d;

    // Sample request on rising edge, synchronous reset clears stored request
    always_ff @(posedge clk) begin
        if (rst) begin
            req_d <= 1'b0;
        end else begin
            req_d <= req;
        end
    end

    // Generate a one‑cycle acknowledgment pulse on the cycle after a request
    // Reset clears the acknowledgment
    always_ff @(posedge clk) begin
        if (rst) begin
            ack <= 1'b0;
        end else begin
            ack <= req_d;
        end
    end
endmodule
