module response_a(input wire clk, rst, req, output reg ack);
    always @(posedge clk)
        if (rst) ack <= 0;
        else ack <= req;
endmodule

module response_b(input wire clk, rst, req, output reg ack);
    reg pending;
    always @(posedge clk) begin
        if (rst) begin pending <= 0; ack <= 0; end
        else begin pending <= req; ack <= pending; end
    end
endmodule
