<<<<<<< Updated upstream
#Victor
=======
def character_occupation_list(file_name: str, occupation: str) -> list[dict]:

    with open(file_name, "r") as inp_file:
        header_line = True
        player_list = []

        for line in inp_file:
            row = line.strip().split(',')

            if header_line:
                keys = row
                header_line = False

            else:
                if row[0] == occupation:
                    row_dict = {}
                    row_dict[keys[1]] = int(row[1])
                    row_dict[keys[2]] = int(row[2])
                    row_dict[keys[3]] = int(row[3])
                    row_dict[keys[4]] = int(row[4])
                    row_dict[keys[5]] = int(row[5])
                    row_dict[keys[6]] = float(row[6])
                    row_dict[keys[7]] = int(row[7])
                    row_dict[keys[8]] = row[8]
                    player_list.append(row_dict)

    inp_file.close()
    return player_list




>>>>>>> Stashed changes
