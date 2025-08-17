import { env } from "@/env.mjs";
import { StateCreator } from "zustand";
import { ChatModel } from "../../../generated";

type State = {
  model: string;
  proMode: boolean;
};

type Actions = {
  setModel: (model: string) => void;
  toggleProMode: () => void;
};

export type ConfigStore = State & Actions;

export const createConfigSlice: StateCreator<
  ConfigStore,
  [],
  [],
  ConfigStore
> = (set) => ({
  model: "hyper",
  proMode: false,
  setModel: (model: string) => set({ model }),
  toggleProMode: () =>
    set((state) => {
      const proModeEnabled = env.NEXT_PUBLIC_PRO_MODE_ENABLED;
      if (!proModeEnabled) {
        return { ...state, proMode: false };
      }
      return { ...state, proMode: !state.proMode };
    }),
});
