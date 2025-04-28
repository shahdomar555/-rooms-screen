import 'package:flutter/material.dart';
import '../models/room.dart';
import 'room_card.dart';

class RoomsWidget extends StatelessWidget {
  const RoomsWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: rooms.length,
      itemBuilder: (context, index) {
        return RoomCard(room: rooms[index]);
      },
    );
  }
}
