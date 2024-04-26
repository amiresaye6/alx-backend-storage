-- Context: Index is not the solution for any performance issue, but well used, it’s really powerful!

CREATE INDEX idx_name_first
ON names (name(1));
