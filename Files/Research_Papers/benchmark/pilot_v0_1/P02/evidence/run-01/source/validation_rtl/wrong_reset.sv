// NEGATIVE CONTROL ONLY: intentionally violates active-high reset.
module p02_wrong(input wire clk, rst, d, output reg q);
    always @(posedge clk) begin
        if (!rst) q <= 1'b0;
        else      q <= d;
    end
endmodule
