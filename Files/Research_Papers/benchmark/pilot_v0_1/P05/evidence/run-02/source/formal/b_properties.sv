// Specification B is two recurrences. Check both, including hold, compositionally.
// pending is a proof-only internal signal; ack remains the only observable.
module p05_b_properties(input wire clk, rst, req, ack, pending);
    reg valid = 0;
    always @($global_clock) begin
        valid <= 1;
        if (valid) begin
            if (!$past(clk) && clk) begin
                assert(pending == ($past(rst) ? 1'b0 : $past(req)));
                assert(ack == ($past(rst) ? 1'b0 : $past(pending)));
            end else begin
                assert(pending == $past(pending));
                assert(ack == $past(ack));
            end
        end
    end
endmodule
